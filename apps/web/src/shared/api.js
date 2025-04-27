
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
			...options,
		})
		.then((response) => response.json())
		.catch((error) => {
			console.error('Request error:', error);
			throw error;
		});
	}
};

export const executeSql = (query) => createRequest ('/sql/execute', {
	method: 'POST',
	body: { query }
})

export const upload = (formData) => createRequest('/files/upload', {
	method: 'POST',
	body: formData,
});