<script>
import { parse } from 'pgsql-ast-parser';
import { executeSql } from '@/shared/api.js';
import { useToast } from 'vue-toastification';

export default {
  name: 'Terminal',
  
  data() {
    return {
      command: '',
      output: [],
      sqlMode: false
    };
  },

  methods: {
    async executeCommand() {
      if (!this.command.trim()) return;

      const prompt = this.sqlMode ? 'SQL >' : '$';
      this.output.push(`${prompt} ${this.command}`);

      const result = await this.processCommand(this.command);
      if (result !== undefined) {
        if (Array.isArray(result)) {
          result.forEach(line => this.output.push(line));
        } else {
          this.output.push(result);
        }
      }

      this.command = '';
      this.$nextTick(() => {
        this.$refs.output.scrollTop = this.$refs.output.scrollHeight;
      });
    },

    async processCommand(command) {
      if (this.sqlMode) return await this.handleSqlCommand(command);
      
      switch (command.trim().toLowerCase()) {
        case 'help': 
          return 'Доступные команды: help, clear, sql';
        case 'clear': 
          this.output = []; 
          return '';
        case 'sql': 
          this.sqlMode = true;
          useToast().info('Режим SQL')
          return 'Режим SQL. Используйте "exit" для выхода';
        default: 
          return `Команда не распознана: "${command}"`;
      }
    },

    async handleSqlCommand(sqlCmd) {
      if (sqlCmd.trim().toLowerCase() === 'exit') {
        this.sqlMode = false;
        useToast().info('Выход из режима SQL')
        return 'Выход из режима SQL';
      } else if (sqlCmd.trim().toLowerCase() === 'clear') {
        this.output = []; 
        return '';
      }

      try {
        parse(sqlCmd);
      } catch (e) {
        return `Ошибка синтаксиса: ${this.formatSqlError(e.message)}`;
      }

      try {
        const response = await executeSql(sqlCmd);
        // добавить обработку ответа
        
      } catch (error) {
        console.error('Ошибка при выполнении запроса:', error);
        return `Ошибка соединения: ${error.message}`;
      }
    },

    formatSqlError(msg) {
      return msg
        .replace(/^error: /i, '')
        .replace(/at position \d+/, '')
        .replace(/line \d+:\d+/, '');
    },

    formatTableOutput(data) {
      if (!Array.isArray(data) || data.length === 0) return ['Нет данных'];
      
      const keys = Object.keys(data[0]);
      const header = keys.join('\t');
      const separator = '-'.repeat(header.length);
      const rows = data.map(row => Object.values(row).join('\t'));

      return [header, separator, ...rows];
    }
  }
};
</script>

<template>
  <div class="terminal">
    <div class="output" ref="output">
      <div v-for="(line, index) in output" :key="index" class="output-line">
        {{ line }}
      </div>
    </div>

    <div class="input">
      <span class="prompt">{{ sqlMode ? 'SQL >' : '$' }}</span>
      <input
        v-model="command"
        @keyup.enter="executeCommand"
        type="text"
        class="command-input"
        :placeholder="sqlMode ? 'Введите SQL-запрос' : 'Введите команду'"
      />
    </div>
  </div>
</template>

<style scoped>
.terminal {
  background-color: #1e1e1e;
  color: #00a94f;
  font-family: monospace;
  padding: 15px;
  border-radius: 5px;
  height: 240px;
  width: 96%;
  display: flex;
  flex-direction: column;
}

.output {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 10px;
  white-space: pre-wrap;
}

.input {
  display: flex;
  align-items: center;
  font-size: 16px;
}

.prompt {
  color: #00a94f;
  margin-right: 5px;
}

.command-input {
  background: none;
  border: none;
  color: #00a94f;
  outline: none;
  flex: 1;
  font-size: 16px;
  font-family: monospace;
}
</style>