<script>
  import Header from './components/Header.vue';
  import Footer from './components/Footer.vue';
  import Terminal from './components/Terminal.vue';
  import ModalUpload from './components/ModalUpload.vue';
  import ModalDownload from './components/ModalDownload.vue';

  export default {
    components: { Header, Footer, Terminal, ModalUpload, ModalDownload },
    data() {
      return {
        uploadModalOpen: false,
        downloadModalOpen: false,
        file: null
      };
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
            <ModalUpload 
              :isOpen="uploadModalOpen" 
              @close="uploadModalOpen = false"
            />

            <button @click="downloadModalOpen = true">Выгрузить</button>
            <ModalDownload 
              :isOpen="downloadModalOpen" 
              @close="downloadModalOpen = false"
            />
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
</style>