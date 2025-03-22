<template>
    <div class="footer">
        <p> &copy; 2025 RUDN </p>
    </div>
</template>
  
<script>
  export default {
    name: 'Footer'
  };
</script>
  
<style scoped>
    .footer {
        flex: 1; 
        padding: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    p {
        margin: 0;
        font-size: 14px;
        font-weight: 200;
    }
</style>