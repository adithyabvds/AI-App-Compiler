import { useState } from "react";
import axios from "axios";

function App() {

  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [viewMode, setViewMode] = useState("text");

  const compileApp = async () => {

    if (!prompt.trim()) {
      alert(
        "Please enter an application description"
      );
      return;
    }

    try {

      const response = await axios.post(
        "https://ai-app-compiler-api-production.up.railway.app/compile",
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
        margin: "auto",
        fontFamily: "Arial"
      }}
    >
      <h1>🚀 AI App Compiler</h1>

      <p>
        Natural Language → Structured Configuration →
        Validation → Repair → Runtime Execution
      </p>

      <textarea
        rows="6"
        value={prompt}
        onChange={(e) =>
          setPrompt(e.target.value)
        }
        placeholder="Describe your application..."
        style={{
          width: "100%",
          padding: "10px",
          borderRadius: "8px"
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

          {/* Output Toggle */}

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

          {/* Text Summary */}

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
                  whiteSpace: "pre-wrap"
                }}
              >
                {
                  result.human_readable_summary ||
                  "No summary available"
                }
              </pre>
            </div>
          )}

          {/* JSON Output */}

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
                  whiteSpace: "pre-wrap"
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

          <br />

          {/* Runtime Proof */}

          <div
            style={{
              border: "1px solid #ddd",
              padding: "15px",
              borderRadius: "8px",
              marginBottom: "15px"
            }}
          >
            <h3>⚙ Runtime Execution Proof</h3>

            <p>
              Runtime:
              {" "}
              {
                result.simulation?.runtime ||
                "N/A"
              }
            </p>

            <p>
              Status:
              {" "}
              {
                result.simulation?.status ||
                "N/A"
              }
            </p>

            <p>
              Tables Created:
              {" "}
              {
                result.simulation?.tables_count ??
                0
              }
            </p>

            <ul>
              {
                result.simulation?.tables_created?.map(
                  (table, index) => (
                    <li key={index}>
                      {table}
                    </li>
                  )
                )
              }
            </ul>
          </div>

          {/* Validation */}

          <div
            style={{
              border: "1px solid #ddd",
              padding: "15px",
              borderRadius: "8px",
              marginBottom: "15px"
            }}
          >
            <h3>✅ Validation Report</h3>

            <p>
              Schema Errors:
              {" "}
              {
                result.validation
                  ?.schema_errors
                  ?.length || 0
              }
            </p>

            <p>
              Consistency Errors:
              {" "}
              {
                result.validation
                  ?.consistency_errors
                  ?.length || 0
              }
            </p>
          </div>

          {/* Repair Engine */}

          <div
            style={{
              border: "1px solid #ddd",
              padding: "15px",
              borderRadius: "8px",
              marginBottom: "15px"
            }}
          >
            <h3>🛠 Repair Engine Proof</h3>

            <p>
              Repairs Performed:
              {" "}
              {
                result.repair?.performed
                  ? "Yes"
                  : "No"
              }
            </p>

            <ul>
              {
                result.repair?.fixes?.map(
                  (fix, index) => (
                    <li key={index}>
                      {fix}
                    </li>
                  )
                )
              }
            </ul>
          </div>

          {/* Domain Coverage */}

          <div
            style={{
              border: "1px solid #ddd",
              padding: "15px",
              borderRadius: "8px"
            }}
          >
            <h3>🌍 Supported Domains</h3>

            <ul>
              <li>CRM Systems</li>
              <li>Hospital Management</li>
              <li>Ecommerce Platforms</li>
              <li>Food Delivery Applications</li>
              <li>Banking Systems</li>
              <li>Inventory Management</li>
              <li>Payroll Systems</li>
              <li>Hotel Booking Systems</li>
              <li>Gym Management</li>
              <li>School Management</li>
              <li>Ride Sharing Platforms</li>
              <li>Social Media Applications</li>
              <li>Logistics Platforms</li>
            </ul>
          </div>
        </>
      )}
    </div>
  );
}

export default App;
