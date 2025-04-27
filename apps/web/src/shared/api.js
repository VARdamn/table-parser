
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


export const getUsers = createRequest('/users', {
	method: 'GET',
	params: {
		gavno: true,
	}
})

export const addUser = createRequest('/users', {
	method: 'POST',
	body: {
		name: 'debil',
		surname: 'eblan',
		email: 'ok@pfur.sru'
	}
})

export const executeSql = (cmd) => createRequest ('/execute', {
	method: 'POST',
	body: {
		cmd: cmd
	}
})

export const upload = (formData) => createRequest('/upload', {
	method: 'POST',
	body: formData,
	headers: {
		
	}
  });