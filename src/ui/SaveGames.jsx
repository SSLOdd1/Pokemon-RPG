import React, { useEffect, useState } from "react";

const saveModules = import.meta.glob("../../saves/*.json", {
	eager: true,
	import: "default",
});

export default function SaveGames({ onSelect }) {
	const [saves, setSaves] = useState([]);
	const [loading, setLoading] = useState(true);
	const [error, setError] = useState("");
	const [selectedId, setSelectedId] = useState(null);

	useEffect(() => {
		let isMounted = true;

		const loadSaves = async () => {
			try {
				setLoading(true);
				setError("");

				const data = Object.entries(saveModules).map(([path, saveData]) => ({
					...(saveData || {}),
					__file: path.split("/").pop(),
				}));
				if (isMounted) {
					setSaves(Array.isArray(data) ? data : []);
				}
			} catch (err) {
				if (isMounted) {
					setError(err?.message || "Unable to load save games.");
				}
			} finally {
				if (isMounted) {
					setLoading(false);
				}
			}
		};

		loadSaves();

		return () => {
			isMounted = false;
		};
	}, []);

	const getSaveId = (save, index) =>
		save?.id ?? save?.name ?? save?.slot ?? save?.metadata?.character_name ?? save?.__file ?? `save-${index}`;

	const getSaveLabel = (save, index) => {
		if (typeof save === "string") return save;
		return save?.name || save?.title || save?.slot || save?.metadata?.character_name || save?.__file || `Save ${index + 1}`;
	};

	const getSaveMeta = (save) => {
		if (!save || typeof save === "string") return "";
		const parts = [
			save?.player || save?.player_data?.name,
			save?.location || save?.metadata?.location,
			save?.updatedAt || save?.lastPlayed || save?.metadata?.save_time,
		].filter(Boolean);
		return parts.join(" • ");
	};

	const handleSelect = (save, index) => {
		const id = getSaveId(save, index);
		setSelectedId(id);
		if (typeof onSelect === "function") {
			onSelect(save);
		}
	};

	return (
		<section className="save-games" aria-label="Save games">
			<h2>Choose a Save Game</h2>

			{loading && <p>Loading saves...</p>}
			{!loading && error && <p role="alert">{error}</p>}

			{!loading && !error && saves.length === 0 && <p>No saves found in the saves folder.</p>}

			{!loading && !error && saves.length > 0 && (
				<ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
					{saves.map((save, index) => {
						const id = getSaveId(save, index);
						const label = getSaveLabel(save, index);
						const meta = getSaveMeta(save);
						const isSelected = selectedId === id;

						return (
							<li key={id} style={{ marginBottom: 8 }}>
								<button
									type="button"
									onClick={() => handleSelect(save, index)}
									aria-pressed={isSelected}
									style={{
										width: "100%",
										textAlign: "left",
										padding: "10px 12px",
										borderRadius: 8,
										border: isSelected ? "2px solid #4a90e2" : "1px solid #ccc",
										background: isSelected ? "#eef5ff" : "#fff",
										cursor: "pointer",
									}}
								>
									<div style={{ fontWeight: 600 }}>{label}</div>
									{meta && (
										<div style={{ fontSize: "0.9rem", opacity: 0.8, marginTop: 2 }}>{meta}</div>
									)}
								</button>
							</li>
						);
					})}
				</ul>
			)}
		</section>
	);
}
