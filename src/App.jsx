import { useRef, useState } from "react";
import MainScreen from "./ui/MainScreen";
import PlayerInput from "./ui/PlayerInput";
import HoverPopup from "./ui/HoverPopup";
import "./app.css";

export default function App() {
  const [hoverText, setHoverText] = useState(null);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const mainScreenRef = useRef(null);

  const handleMouseMove = (e) => {
    setMousePos({ x: e.clientX, y: e.clientY });
  };

  return (
    <div className="app-container" onMouseMove={handleMouseMove}>
      <MainScreen ref={mainScreenRef} setHoverText={setHoverText} />
      <PlayerInput setHoverText={setHoverText} />
      <HoverPopup
        hoverText={hoverText}
        mousePos={mousePos}
        mainScreenRef={mainScreenRef}
      />
    </div>
  );
}
