import React, { useState } from "react";
import axios from "axios";

function App() {
  const [resume, setResume] = useState("");
  const [jobs, setJobs] = useState([]);

  const handleClick = async () => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/recommend",
        null,
        {
          params: { resume_text: resume },
        }
      );
      setJobs(response.data);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>AI Job Recommendation System</h1>

      <textarea
        rows="5"
        cols="50"
        placeholder="Paste your resume text here..."
        value={resume}
        onChange={(e) => setResume(e.target.value)}
      />

      <br /><br />

      <button onClick={handleClick}>
        Recommend Jobs
      </button>

      <div style={{ marginTop: "30px" }}>
        {jobs.map((job, index) => (
          <div key={index}>
            <h3>{job.job_title}</h3>
            <p>{job.company}</p>
            <hr />
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;