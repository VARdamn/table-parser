<template>
  <div class="header">
    <img src="/src/assets/logo_rudn.png" width="140px" alt="Логотип">
  </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style scoped>
.header {
  flex: 1;
  padding: 15px;
  box-shadow: 0px 0px 26px 8px rgba(156, 156, 156, 0.26);
  display: flex;
  align-items: center;
}

.header img {
  margin-right: 20px ;
}

.header p {
  margin: 0;
}

</style>