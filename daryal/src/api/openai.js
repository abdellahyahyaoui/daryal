import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

export const iniciarDiagnostico = async (datosVehiculo) => {
    try {
        const response = await axios.post(`${API_URL}/iniciar-diagnostico`, datosVehiculo);
        return response.data;
    } catch (error) {
        console.error("Error al iniciar el diagnóstico:", error);
        throw error;
    }
};

export const continuarDiagnostico = async (historial, vehiculo) => {
    try {
        const response = await axios.post(`${API_URL}/continuar-diagnostico`, { historial, vehiculo });
        return response.data;
    } catch (error) {
        console.error("Error al continuar el diagnóstico:", error);
        throw error;
    }
};