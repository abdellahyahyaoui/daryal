import React, { useState } from 'react';
import WelcomeDialog from '../WelcomeDialog/WelcomeDialog';
import VehicleForm from '../VehicleForm/VehicleForm';
import QuestionForm from '../QuestionForm/QuestionForm';
import Diagnosis from '../Diagnosis/Diagnosis';
import { iniciarDiagnostico, continuarDiagnostico } from '../../api/openai';
import './Home.css'
function Home() {
  const [step, setStep] = useState('welcome');
  const [vehicleData, setVehicleData] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState('');
  const [questionCount, setQuestionCount] = useState(0);
  const [historial, setHistorial] = useState([]);
  const [diagnosis, setDiagnosis] = useState('');
  const [isLastQuestion, setIsLastQuestion] = useState(false);


  const handleStartDiagnosis = () => setStep('vehicleForm');

  const handleVehicleSubmit = async (data) => {
    setVehicleData(data);
    try {
      const response = await iniciarDiagnostico(data);
      setCurrentQuestion(response.pregunta);
      setHistorial([...historial, { tipo: 'problema', texto: data.problema }]);
      setStep('questions');
    } catch (error) {
      console.error("Error al iniciar el diagnóstico:", error);
    }
  };

  const handleQuestionSubmit = async (answer) => {
  const updatedHistorial = [...historial, { tipo: 'pregunta', texto: currentQuestion }, { tipo: 'respuesta', texto: answer }];
  setHistorial(updatedHistorial);
  setQuestionCount(questionCount + 1);

  try {
    const response = await continuarDiagnostico(updatedHistorial, vehicleData);
    if (response.pregunta) {
      setCurrentQuestion(response.pregunta);
      if (response.es_ultima) {
        setIsLastQuestion(true);
      }
    } else if (response.diagnostico_y_soluciones) {
      setDiagnosis(response.diagnostico_y_soluciones);
      setStep('diagnosis');
    }
  } catch (error) {
    console.error("Error al continuar el diagnóstico:", error);
  }
};

  return (
    <div className="home">
      {step === 'welcome' && <WelcomeDialog onStart={handleStartDiagnosis} />}
      {step === 'vehicleForm' && <VehicleForm onSubmit={handleVehicleSubmit} />}
      {step === 'questions' && (
        <QuestionForm
          question={currentQuestion}
          onSubmit={handleQuestionSubmit}
          questionNumber={questionCount + 1}
          maxQuestions={5}
        />
      )}
      {step === 'diagnosis' && <Diagnosis diagnosis={diagnosis} />}
    </div>
  );
}

export default Home;