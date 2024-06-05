import React, { useState } from "react";
import axios from "axios";



const Search= () => {
  const [query, setQuery] = useState("");
  const [output, setOutput] = useState("");

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setQuery(event.target.value);
  };
  const [loading, setLoading] = useState(false);

  const handleSearch = () => {
    let data;
    setLoading(true); // Set loading state to true
    axios
      .post(`http://127.0.0.1:8000/`, { query })
      .then((response) => {
        console.log(response.data);
        setOutput(response.data)

      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      })
      .finally(() => {
        setLoading(false); // Set loading state back to false when the request completes
      });
  };

  return (
    <div className="relative">
      <div className="flex items-center justify-center">

        <input
          type="text"
          placeholder="Ask a question...."
          className="px-4 py-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 focus:outline-none w-64"
          value={query}
          onChange={handleInputChange}
        />
        <button
          className={`px-4 py-2 rounded-md ml-2 ${
            loading ? "bg-blue-500" : "bg-blue-600"
          } text-white`}
          onClick={handleSearch}
          disabled={loading}
        >
          {loading ? (
            <svg
              className="animate-spin h-5 w-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
            >
            </svg>
          ) : (
            "Search"
          )}
        </button>
      </div>

      <div>
      <header> Generated from django</header>
      {output.output}
      <div class = "border-solid border-2 border-indigo-600">
      {output.explanation}
      </div>
      <div>
      {output.pesudo_code}
      </div>
      
    </div>
        
        
    </div>
  );
};

export default Search