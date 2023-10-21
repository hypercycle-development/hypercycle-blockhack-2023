import { useRef, useState } from "react";
import Layout from "./layout";

function App() {
  const [greeting, setGreeting] = useState("");

  const handleClick = async () => {
    // Here you can change the API endpoint
    const imagePost = await fetch("api/greet", {
      method: "get",
    });
    const response = await imagePost.json();
    setGreeting(response.text);
  };
  return (
    <>
      <Layout>
        <div className="flex min-h-[calc(100vh-100px)]  w-full flex-col items-center bg-gray-950 text-gray-300">
          <div className="mt-8 text-xl font-bold text-gray-400">
            Welcome to the Greeting example.
          </div>
          <div className="min-h-60 mb-14 mt-16 w-[600px] rounded-xl border-2 border-gray-700 p-4">
            <div className="mb-8 text-lg font-bold">AI Communications</div>
            <button
              onClick={handleClick}
              className="inline-flex items-center rounded-xl border border-green-800 bg-green-400 px-5 py-2 text-center text-lg font-medium text-green-950 transition-all duration-200 hover:border-green-700  hover:bg-green-500 hover:text-green-950 focus:outline-none focus:ring-1 focus:ring-green-600"
            >
              Greet
            </button>
            {greeting ? (
              <div className="w-full text-center text-lg text-gray-400">
                {greeting}
              </div>
            ) : (
              ""
            )}
          </div>
        </div>
      </Layout>
    </>
  );
}

export default App;
