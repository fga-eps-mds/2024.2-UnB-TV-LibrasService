import React, { useState, useEffect } from "react";

const App = () => {
  const [widget, setWidget] = useState("");

  useEffect(()=>{
    fetch("http://backend:800/vlibras-widget", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: "Texto inicial para Linre" }),
    })
      .then((response) => response.json())
      .then((data) => setWidget(data.widget))
      .catch((error) => console.error("Erro ao carregar o widget:", error));
  }, []);

  return (
    <div>
      <h1>VLibras Widget</h1>
      <div dangerouslySetInnerHTML={{ __html: widget }} />
    </div>
  );
};

export default App;