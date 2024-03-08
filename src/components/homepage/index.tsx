import React, { useState } from "react";
import "./styles.css";

const HomePage = () => {
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  
  const fetchData = async () => {
    setLoading(true);
    try {
      const response = await fetch(process.env.REACT_APP_LAMBDA_URL ?? "");

      if (response.ok) {
        const data = await response.json();
        setMessage(data.message);
        setLoading(false);
      } else {
        console.error("Failed to fetch");
      }
    } catch (error) {
      console.error("Error fetching ", error);
    }
  };

  return (
    <div className="container">
      <button
      className="btn"
        onClick={fetchData}
      >
        Fetch Data
      </button>
      {!loading ? (
        <img 
        className="image"
        src={message} />
      ) : (
        <svg viewBox="25 25 50 50">
          <circle r="20" cy="50" cx="50"></circle>
        </svg>
      )}
    </div>
  );
};

export default HomePage;
