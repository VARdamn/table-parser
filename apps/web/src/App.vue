<script>
  import Header from './components/Header.vue';
  import Footer from './components/Footer.vue';
  import Terminal from './components/Terminal.vue';
  import Modal from './components/ModalWindow.vue';

  export default {
    components: { Header, Footer, Terminal, Modal },
    data() {
      return {
        uploadModalOpen: false,
        downloadModalOpen: false,
        file: null
      };
    },
    methods: {
      handleUpload() {
        console.log('Загружаем файл:', this.file);
        // дописать
        this.isModalOpen = false;
      }, 
      
      handleFileSelect(event) {
        this.file = event.target.files[0];
      },

      removeFile() {
        this.file = null;
        // Очищаем значение input, чтобы можно было выбрать тот же файл снова
        const input = this.$el.querySelector('input[type="file"]');
        if (input) input.value = '';
      },

      formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
      },

      handleUpload() {
        
        // Логика загрузки файла

        console.log('Загружаем файл:', this.file);
        this.file = null;
        this.isModalOpen = false;

      },

      handleDownload() {
        
        // Логика скачивания файла

        console.log('Скачиваем файл:');
        this.file = null;
        this.isModalOpen = false;

      }
    }
  };
</script>

<template>
  <div class="page">
    <Header />
    <main class="main-content">
      <div class="container">
        
        <div class="title">
          <h1>Управление базой данных</h1>
        </div>
        
        <div class="wrapper">
          <h3>Выберите действие</h3>
          
          <div class="block-buttons">
            <button @click="uploadModalOpen = true">Загрузить</button>
            <Modal :isOpen="uploadModalOpen" @close="uploadModalOpen=false" width="600px">
              <template #header>
                <h3>Загрузить файл</h3>
              </template>

              <div class="file-upload-content">
                <label class="input-file">
                  <input type="file" @change="handleFileSelect">
                  <div class="input-file-text">
                    <span>+</span>
                    <h4>Выберите файл для загрузки</h4>
                  </div>
                </label>
                
                <div v-if="file" class="file-info">
                  <div class="file-icon">
                    <svg viewBox="0 0 24 24" width="24" height="24">
                      <path d="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M18,20H6V4H13V9H18V20Z" />
                    </svg>
                  </div>
                  <div class="file-details">
                    <div class="file-name">{{ file.name }}</div>
                    <div class="file-size">{{ formatFileSize(file.size) }}</div>
                  </div>
                  <button @click="removeFile" class="remove-btn">×</button>
                </div>
              </div>

              <template #footer>
                <button class="save" @click="handleUpload" :disabled="!file">Сохранить</button>
                <button class="cancel" @click="uploadModalOpen = false">Отменить</button>
              </template>
            </Modal>

            <button @click="downloadModalOpen = true">Выгрузить</button>
            <Modal :isOpen="downloadModalOpen" @close="downloadModalOpen=false" width="600px">
              <template #header>
                <h3>Скачать файл</h3>
              </template>

              <div class="file-download-content">
                  <div class="download-file-text">
                    <h4>Выберите файл для скачивания</h4>
                  </div>
                
                   <!-- доделать список доступных файлов  -->

              </div>

              <template #footer>
                <button class="save" @click="handleDownload" :disabled="!file">Скачать</button>
                <button class="cancel" @click="downloadModalOpen = false">Отменить</button>
              </template>
            </Modal>
          </div>
          
          <h3>...или воспользуйтесь терминалом</h3>
          <Terminal />
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<style scoped>
  .page {
    display: flex;
    flex-direction: column;
    flex-shrink: 0;
    min-height: 100vh; /* Минимальная высота = весь экран */
    margin: 0;
    padding: 0;
  }

  .main-content {
    flex: 1; /* Занимает всё доступное пространство между Header и Footer */
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
    max-height: calc(100vh - 110px); 
  }

  .container {
    display: flex;
    width: 100%;
    max-width: 1200px; /* Ограничиваем ширину контейнера */
    gap: 20px;
  }

  .title {
    flex: 1;
    padding: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .wrapper {
    flex: 2;
    background-color: #ffffff;
    padding: 0px 20px 20px 20px;
    border-radius: 9px;
    box-shadow: 0px 0px 26px 8px rgba(156, 156, 156, 0.26);
    font-size: 14px;
  }

  .block-buttons {
    display: flex;
    gap: 10px;
    margin-top: 10px;
  }

  .file-upload-content, .file-download-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    gap: 1.5rem;
  }

  .input-file {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100px;
    border: 2px dashed #ccc;
    border-radius: 8px;
    background-color: #f3f4f5;
    transition: all 0.3s ease;
    cursor: pointer;
    text-align: center;
    padding: 1rem;
  }

  .input-file:hover {
    border-color: #00a94f;
    background-color: #f0f8f3;
  }

  .input-file-text {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    color: #555;
  }

  .download-file-text {
    display: flex;
    flex-direction: column;
    align-items: left;
    gap: 0.5rem;
    color: #555;
  }

  .input-file-text span {
    width: 48px;
    height: 48px;
    color: #00a94f;
    font-size: 48px;
  }

  .input-file-text h4 {
    margin: 0;
    font-size: 1.2rem;
  }

  .input-file-text p {
    margin: 0;
    font-size: 0.9rem;
    color: #777;
  }

  /* Скрытие стандартного input */
  .input-file input[type="file"] {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    border: 0;
  }

  /* Стили для отображения выбранного файла */
  .file-info {
    width: 100%;
    padding: 1rem;
    background-color: #f3f4f5;
    border-radius: 8px;
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .file-info button {
    background: none;
    border: none;
    font-size: 24px;
    cursor: pointer;
    color: rgba(15, 15, 15, 0.87);
  }

  .file-info button:focus, button:focus-visible {
    outline: 0px;
  }

  .file-icon {
    color: #42b983;
    font-size: 1.5rem;
  }

  .file-details {
    flex-grow: 1;
  }

  .file-name {
    font-weight: 500;
    margin-bottom: 0.3rem;
  }

  .file-size {
    color: #666;
    font-size: 0.8rem;
  }
</style>