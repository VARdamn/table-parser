<script>
  export default {
    name: 'Terminal',

    data() {
      return {
        command: '', // Текущая команда
        output: [], // Массив для хранения вывода
      };
    },

    methods: {
      executeCommand() {
        if (this.command.trim() === '') return; // Игнорируем пустые команды
  
        // Добавляем введенную команду в вывод
        this.output.push(`$ ${this.command}`);
  
        // Обрабатываем команду
        const result = this.processCommand(this.command);
        this.output.push(result);
  
        // Очищаем поле ввода
        this.command = '';
  
        // Прокручиваем вывод вниз
        this.$nextTick(() => {
          this.$refs.output.scrollTop = this.$refs.output.scrollHeight;
        });
      },

      processCommand(command) {
        switch (command.trim()) {
          case 'help':
            return 'Доступные команды: help, clear.';
          case 'clear':
            this.output = [];
            return '';
          default:
            console.log(command);
            return `Команда не распознана: "${command}"`;
        }
      },
    },
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
        <span class="prompt">$</span>
        <input
          v-model="command"
          @keyup.enter="executeCommand"
          type="text"
          class="command-input"
          placeholder="Введите команду"
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
    height: 300px;
    width: 95%;
    display: flex;
    flex-direction: column;
  }
  
  .output {
    flex: 1; /* Занимает всё доступное пространство */
    overflow-y: auto; /* Прокрутка, если вывод слишком большой */
    margin-bottom: 10px;
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
