import React, { useState } from 'react';
import './QuestionForm.scss';

function QuestionForm({ question, questionNumber, maxQuestions, onSubmit, isLastQuestion }) {
  const [answer, setAnswer] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    onSubmit(answer);
    setAnswer('');
  };

  return (
    <form className="question-form" onSubmit={handleSubmit}>
      <h2>Pregunta {questionNumber} de {maxQuestions}</h2>
      <p>{question}</p>
      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
        placeholder="Tu respuesta"
        required
      ></textarea>
      <button type="submit">
        {isLastQuestion ? "Finalizar" : "Siguiente"}
      </button>
    </form>
  );
}

export default QuestionForm;