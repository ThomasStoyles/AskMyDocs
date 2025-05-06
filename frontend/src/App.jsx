import { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  const upload = async () => {
    const form = new FormData();
    form.append("file", file);
    await fetch("http://localhost:8000/upload/", {
      method: "POST",
      body: form
    });
    alert("PDF uploaded!");
  };

  const ask = async () => {
    setLoading(true);
    const form = new FormData();
    form.append("question", question);
    const res = await fetch("http://localhost:8000/ask/", {
      method: "POST",
      body: form
    });
    const data = await res.json();
    setAnswer(data.answer);
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Ask My Docs</h1>
      <input type="file" onChange={e => setFile(e.target.files[0])} />
      <button onClick={upload}>Upload PDF</button>

      <div>
        <input
          placeholder="Ask a question..."
          value={question}
          onChange={e => setQuestion(e.target.value)}
        />
        <button onClick={ask}>Ask</button>
      </div>

      {loading ? <p>Loading...</p> : <p><b>Answer:</b> {answer}</p>}
    </div>
  );
}

export default App;
