<script>
  export default {
    name: 'Header',
  };
</script>

<template>
  <div class="header">
    <img src="/src/assets/logo_rudn.png" width="140px" alt="Логотип">
  </div>
</template>

<style scoped>
  .header {
    height: 40px;
    padding: 15px;
    box-shadow: 0px 0px 26px 8px rgba(156, 156, 156, 0.26);
    display: flex;
    align-items: center;
    flex-shrink: 0;
  }

  .header img {
    margin-right: 20px;
  }
</style>