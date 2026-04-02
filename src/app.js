// App.js
import { useState } from "react";
import "./App.css";

export default function App() {
  const [hoverData, setHoverData] = useState(null);

  return (
    <div className="app-container">
      <div 
        className="main-screen"
        onMouseEnter={() => setHoverData("Main screen info")}
        onMouseLeave={() => setHoverData(null)}
      >
        Main Screen
      </div>

      <div 
        className="player-input"
        onMouseEnter={() => setHoverData("Player input info")}
        onMouseLeave={() => setHoverData(null)}
      >
        Player Input
      </div>

      {hoverData && (
        <div className="hover-popup">
          {hoverData}
        </div>
      )}
    </div>
  );
}
