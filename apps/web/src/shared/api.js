
const createRequest = (endpoint, options = {}) => {  
	const defaultHeaders = {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
	};

	const QS = options.params ? `?${new URLSearchParams(options.params).toString()}` : ''
	
	return async () => {
		return fetch(
			`${import.meta.env.VITE_BACKEND_URL}${endpoint}${QS}`, {
			method: options.method || 'GET', 
			headers: {
				...defaultHeaders,
				...options.headers,
			},
			body: options.body ? JSON.stringify(options.body) : undefined,
		})
		.then((response) => response.json())
		.catch((error) => {
			console.error('Request error:', error);
			throw error;
		});
	}
};

const executeSql = async (query) => await createRequest('/sql/execute', {
	method: 'POST',
	body: { query }
})()

const uploadFile = (formData) => createRequest('/files/upload', {
	method: 'POST',
	body: formData,
});

const getSpecializations = async () => await createRequest('/specializations', {
	method: 'GET',
})()

const getGroups = async () => await createRequest('/groups', {
	method: 'GET',
})()

const getSubjects = async () => await createRequest('/subjects', {
	method: 'GET',
})()

const getTeachers = async () => await createRequest('/teachers', {
	method: 'GET',
})()


export const $$api = {
	getSpecializations,
	getGroups,
	getSubjects,
	getTeachers,
	
	executeSql,
	uploadFile
}