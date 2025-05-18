<script>
  	import Modal from './ModalWindow.vue';
    import { useToast } from 'vue-toastification';
	import { $$api } from '@/shared/api';
	
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
				selectedTableId: '',
				selectedTable: null,
				availableTables: [
					{ id: 'teachers', name: 'Преподаватели' },
					{ id: 'groups', name: 'Группы' },
					{ id: 'subjects', name: 'Предметы' },
					{ id: 'specializations', name: 'Направления' }
				]
			}
		},
		
		watch: {
			selectedTableId(newId) {
				if (newId) {
					this.fetchTableData(newId);
				} else {
					this.selectedTable = null;
				}
			}
		},
		
		methods: {
			close() {
				this.$emit('close');
			},

			async fetchTableData(tableId) {
				const toast = useToast();
				try {
					let data;
					switch (tableId) {
					case 'teachers':
						data = await $$api.getTeachers();
						break;
					case 'groups':
						data = await $$api.getGroups();
						break;
					case 'subjects':
						data = await $$api.getSubjects();
						break;
					case 'specializations':
						data = await $$api.getSpecializations();
						break;
					default:
						data = [];
					}

					const tableInfo = this.availableTables.find(t => t.id === tableId);

					this.selectedTable = {
						...tableInfo,
						rows: data.length,
						created_at: data[0]?.created_at
					};
				} catch (error) {
					console.log(error);
					toast.error('Ошибка загрузки данных таблицы');
					this.selectedTable = null;
				}
			},

			handleDownload() {
				const toast = useToast()
				console.log('Скачиваем: '+ this.selectedTable.name);

				// логика скачивания

				toast.success('Файл успешно сохранен!')
				this.selectedTable = null;
				this.close();
			}
		}
	};
</script>

<template>
    <Modal :isOpen="isOpen" @close="close" width="600px">
      <template #header>
        <h3>Скачать файл</h3>
      </template>
  
      <div class="file-download-content">
            <div class="select-wrapper">
                <h4 class="file-download-text">Выберите таблицу для скачивания:</h4>
				<select 
					id="table-select"
					v-model="selectedTableId"
					class="table-select"
				>
					<option disabled value="">Выберите из списка</option>
					<option 
						v-for="table in availableTables" 
						:key="table.id"
						:value="table.id"
					>
						{{ table.name }}
					</option>
				</select>

            </div>

            <div v-if="selectedTable" class="table-info">
                <div class="info-row">
                    <span class="info-label">Название:</span>
                    <span>{{ selectedTable.name }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Количество строк:</span>
                    <span>{{ selectedTable.rows }}</span>
                </div>
				<div class="info-row" v-if="selectedTable.created_at">
					<span class="info-label">Дата создания:</span>
					<span>{{ selectedTable.created_at }}</span>
				</div>
            </div>
        </div>
  
      <template #footer>
        <button class="save" @click="handleDownload" :disabled="!selectedTable">Скачать</button>
        <button class="cancel" @click="close">Отменить</button>
      </template>
    </Modal>
</template>
  
<style scoped>
  .file-download-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
    gap: 1.5rem;
  }
  
  .file-download-text {
    display: flex;
    flex-direction: column;
    align-items: left;
    gap: 0.5rem;
    color: #555;
  }

  .select-wrapper {
    width: 100%;
    margin-bottom: 10px;
  }
  
  .table-select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 6px;
    background-color: white;
    font-size: 14px;
    margin-top: 5px;
  }
  
  .table-select:focus {
    outline: none;
    border-color: #00a94f;
    box-shadow: 0 0 0 2px rgba(66, 185, 131, 0.2);
  }
  
  .table-info {
    background-color: #f0f8f3;
    border-radius: 6px;
    padding: 15px;
    margin-top: 10px;
    width: 90%;
  }
  
  .info-row {
    display: flex;
    margin-bottom: 8px;
  }
  
  .info-label {
    font-weight: 600;
    min-width: 150px;
    color: #555;
  }
</style>