<script>
    export default {
        props: {
        isOpen: { type: Boolean, default: false },
        width: { type: String, default: '500px' },
        closeOnOverlayClick: { type: Boolean, default: true }
        },

        methods: {
            close() {
            this.$emit('close');
        },
            handleOverlayClick() {
            if (this.closeOnOverlayClick) this.close();
        }
        }
    };
</script>


<template>
    <div v-if="isOpen" class="modal-overlay" @click.self="handleOverlayClick">
      <div class="modal" :style="{ width: width }">

        <header v-if="$slots.header" class="modal-header">
          <slot name="header"></slot>
          <button class="close-btn" @click="close">×</button>
        </header>
  
        <!-- Основное содержимое -->
        <div class="modal-body">
          <slot></slot>
        </div>
  
        <!-- Футер (опциональный) -->
        <footer v-if="$slots.footer" class="modal-footer">
          <slot name="footer"></slot>
        </footer>
      </div>
    </div>
</template>
  
<style scoped>
    .modal-overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0, 0, 0, 0.5);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
    }
    
    .modal {
        background: white;
        border-radius: 8px;
        box-shadow: 0 2px 10px rgba(39, 39, 39, 0.1);
        max-height: 90vh;
        overflow-y: auto;
    }
    
    .modal-header {
        padding-left: 15px;
        border-bottom: 1px solid #eee;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .modal-body {
        padding: 20px;
    }
    
    .modal-footer {
        padding: 16px;
        border-top: 1px solid #eee;
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    
    .modal button {
        background: none;
        border: none;
        font-size: 24px;
        cursor: pointer;
        color: rgba(15, 15, 15, 0.87);
    }

    .modal button:focus, button:focus-visible {
        outline: 0px;
    }
</style>