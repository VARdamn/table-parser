<script>
    import Modal from './ModalWindow.vue';
    import { upload } from '@/shared/api.js'
    
    export default {
        components: { Modal },
        props: {
            isOpen: {
            type: Boolean,
            required: true
            }
        },

        data() {
            return {
                file: null
            };
        },

        methods: {
            close() {
                this.$emit('close');
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

            async handleUpload() {
                if (!this.file) return;
                try {
                    const formData = new FormData();
                    formData.append('file', this.file);
                    console.log('Загружаем файл:', this.file);
                    this.file = null;
                    const response = upload(formData);
                    console.log(response);
                    // обработка успешной загрузки

                } catch (error) {
                    // обработка ошибок
                }
            }
        }
    };
</script>

<template>
    <Modal :isOpen="isOpen" @close="close" width="600px">
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
            <button class="cancel" @click="close">Отменить</button>
        </template>
    </Modal>
</template>

<style scoped>
    .file-upload-content {
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