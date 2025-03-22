<script>
import Header from './components/Header.vue';
import Footer from './components/Footer.vue';
import Terminal from './components/Terminal.vue';

export default {
  components: { Header, Footer, Terminal }
}
</script>

<template>
  <body>
    <div class="page">
      <Header />
      <div class="container">
        <div class="title">
          <h1> Управление базой данных </h1>
        </div>

        <div class="wrapper">
          <h3> Выберите действие </h3>

          <div class="block-buttons">
            <button> Загрузить </button>
            <button> Выгрузить </button>
          </div>

          <h3>...или воспользуйтесь терминалом</h3>
          <Terminal />
        </div>
      </div>
      <Footer />
    </div>

  </body>
</template>

<style scoped>
  .page {
    display: flex;
    flex-direction: column; /* Располагаем элементы вертикально */
    align-items: stretch; /* Центрируем по горизонтали */
    justify-content: center; /* Центрируем по вертикали */
    width: 100%;  /* Ширина 100% ширины окна */
    height: 100vh; /* Высота страницы равна высоте экрана */
    overflow: hidden; /* Убираем прокрутку */
    box-sizing: border-box; /* Учитываем padding в ширине */
  }

  .container {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%; /* Контейнер на всю ширину страницы */
    height: 100vh;
    gap: 20px; /* Расстояние между блоками */
    padding: 20px;
    box-sizing: border-box;
  }

  .title {
    flex: 1; /* Занимает 1 часть (1/3) */
    padding: 20px; /* Внутренние отступы */
  }

  .wrapper {
    flex: 2; /* Занимает 2 части (2/3) */
    background-color: #ffffff;
    padding-left: 20px; 
    padding-bottom: 20px; 
    border-radius: 9px; 
    box-shadow: 0px 0px 26px 8px rgba(156, 156, 156, 0.26);
  }

  .block-buttons {
    display: flex;
    gap: 10px; 
    margin-top: 10px;
  }
</style>