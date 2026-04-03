import { useRef, useState } from "react";
import { HoverPopup, MainScreen, PlayerInput, SaveGames, StartMenu } from "./ui/index.js";
import "./app.css";

export default function App() {
  const [view, setView] = useState("menu");
  const [selectedSave, setSelectedSave] = useState(null);
  const [hoverText, setHoverText] = useState(null);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const mainScreenRef = useRef(null);

  const handleMouseMove = (e) => {
    setMousePos({ x: e.clientX, y: e.clientY });
  };

  return (
    <div className="app-container" onMouseMove={handleMouseMove}>
      {view === "menu" && (
        <StartMenu
          onNewGame={() => {
            setSelectedSave(null);
            setView("game");
          }}
          onLoadGame={() => setView("load")}
          onOptions={() => {
            // Placeholder for future options menu
            alert("Options menu is not implemented yet.");
          }}  
        />
      )}

      {view === "load" && (
        <div style={{ width: "100%", maxWidth: 720, margin: "2rem auto", padding: "0 1rem" }}>
          <button
            type="button"
            onClick={() => setView("menu")}
            style={{ marginBottom: "1rem", padding: "0.5rem 0.75rem", cursor: "pointer" }}
          >
            Back
          </button>
          <SaveGames
            onSelect={(save) => {
              setSelectedSave(save);
              setView("game");
            }}
          />
        </div>
      )}

      {view === "game" && (
        <>
          <MainScreen ref={mainScreenRef} setHoverText={setHoverText} selectedSave={selectedSave} />
          <PlayerInput setHoverText={setHoverText} />
          <HoverPopup
            hoverText={hoverText}
            mousePos={mousePos}
            mainScreenRef={mainScreenRef}
          />
        </>
      )}
    </div>
  );
}
