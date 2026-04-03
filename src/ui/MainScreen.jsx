import { forwardRef } from "react";

const locationDetails = {
  "Greenwood Village": {
    description:
      "A peaceful village surrounded by lush forests. The villagers are friendly and often have quests for adventurers. Includes a basic blacksmith, a general store, and a tavern.",
  },
  "Greenwood Tavern": {
    description:
      "A lively tavern where adventurers can gather to share stories, find new quests, and enjoy a drink. The tavern is run by a jovial innkeeper who is always eager to hear about the latest adventures.",
  },
  "Greenwood Tavern Basement": {
    description:
      "A dimly lit basement beneath the tavern. It is rumored to be haunted, and some say that strange noises can be heard coming from down there at night.",
  },
  "Greenwood Forest": {
    description:
      "A dense and mysterious forest that surrounds Greenwood Village. It is home to a variety of creatures, some friendly and some hostile.",
  },
};

const MainScreen = forwardRef(function MainScreen({ selectedSave }, ref) {
  const currentLocation = selectedSave?.metadata?.location ?? "Greenwood Village";
  const currentDescription =
    locationDetails[currentLocation]?.description ??
    "A peaceful village surrounded by lush forests. The villagers are friendly and often have quests for adventurers. Includes a basic blacksmith, a general store, and a tavern.";

  return (
    <div
      ref={ref}
      className="main-screen"
    >
      <div className="main-menu-card">
        <div className="main-menu-header">
          <p className="main-menu-kicker">Adventure Log</p>
          <h2>Main Menu</h2>
          <p className="main-menu-subtitle">Choose an action to continue your journey.</p>
        </div>

        <div className="main-menu-location">
          <p className="main-menu-location-label">You are currently at:</p>
          <h3>{currentLocation}</h3>
          <p className="main-menu-location-description">{currentDescription}</p>
        </div>

        <div className="main-menu-divider" />
      </div>
    </div>
  );
});

export default MainScreen;
