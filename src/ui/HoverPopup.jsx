export default function HoverPopup({ hoverText, mousePos, mainScreenRef }) {
  if (!hoverText || !mainScreenRef.current) return null;

  const rect = mainScreenRef.current.getBoundingClientRect();
  const bottomThirdStart = rect.top + rect.height * (2 / 3);
  const clampedY = Math.max(mousePos.y + 12, bottomThirdStart);

  return (
    <div
      className="hover-popup"
      style={{
        top: clampedY,
        left: mousePos.x + 12,
      }}
    >
      {hoverText}
    </div>
  );
}
