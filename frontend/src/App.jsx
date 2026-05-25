import { useState } from "react";
import axios from "axios";

function App() {

  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [viewMode, setViewMode] = useState("text");

  const compileApp = async () => {

    try {

      const response = await axios.post(
        "http://127.0.0.1:8000/compile",
        {
          prompt: prompt
        }
      );

      setResult(response.data);

    } catch (error) {

      console.error(error);

      alert(
        "Failed to compile application"
      );
    }
  };

  return (
    <div
      style={{
        padding: "20px",
        maxWidth: "1200px",
        margin: "auto"
      }}
    >
      <h1>🚀 AI App Compiler</h1>

      <textarea
        rows="6"
        cols="80"
        value={prompt}
        onChange={(e) =>
          setPrompt(e.target.value)
        }
        placeholder="Describe your application..."
        style={{
          width: "100%",
          padding: "10px"
        }}
      />

      <br />
      <br />

      <button
        onClick={compileApp}
        style={{
          padding: "10px 20px",
          cursor: "pointer"
        }}
      >
        Compile App
      </button>

      {result && (
        <>
          <br />
          <br />

          <div
            style={{
              display: "flex",
              gap: "10px"
            }}
          >
            <button
              onClick={() =>
                setViewMode("text")
              }
            >
              📄 Text Summary
            </button>

            <button
              onClick={() =>
                setViewMode("json")
              }
            >
              📦 JSON Output
            </button>
          </div>

          <br />

          {viewMode === "text" && (

            <div
              style={{
                border: "1px solid #ccc",
                padding: "15px",
                borderRadius: "8px",
                background: "#f8f8f8"
              }}
            >
              <pre
                style={{
                  whiteSpace:
                    "pre-wrap"
                }}
              >
                {
                  result.human_readable_summary ||
                  "No summary available"
                }
              </pre>
            </div>

          )}

          {viewMode === "json" && (

            <div
              style={{
                border: "1px solid #ccc",
                padding: "15px",
                borderRadius: "8px",
                background: "#f8f8f8"
              }}
            >
              <pre
                style={{
                  whiteSpace:
                    "pre-wrap"
                }}
              >
                {
                  JSON.stringify(
                    result,
                    null,
                    2
                  )
                }
              </pre>
            </div>

          )}

        </>
      )}
    </div>
  );
}

export default App;