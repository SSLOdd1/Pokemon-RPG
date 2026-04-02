import { forwardRef } from "react";

const MainScreen = forwardRef(function MainScreen({ setHoverText }, ref) {
  return (
    <div
      ref={ref}
      className="main-screen"
      onMouseEnter={() => setHoverText("This is the main screen")}
      onMouseLeave={() => setHoverText(null)}
    >
      <h2>Main Screen</h2>
      {/* Render game content here */}
    </div>
  );
});

export default MainScreen;
