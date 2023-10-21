import { useRef, useState } from "react";
import Layout from "./layout";

function App() {
  const [file, setFile] = useState<File | undefined>();
  const [dataBase64, setDataBase64] = useState<any>(undefined);
  const [dataError, setDataError] = useState<any>();
  const [loading, setLoading] = useState<boolean>(false);
  const [translatedImg, setTranslatedImg] = useState<any | undefined>(
    undefined,
  );

  const canvasRef = useRef<HTMLCanvasElement>(null);
  const translatedCanvasRef: any = useRef();
  function handleOnChange(e: React.FormEvent<HTMLInputElement>) {
    const target = e.target as HTMLInputElement & {
      files: FileList;
    };
    console.log(target.value);
    const reader = new FileReader();
    reader.onload = () => {
      const img: any = new Image();
      img.src = reader.result;
      img.onload = () => {
        if (canvasRef.current) {
          img.width = 500;
          img.height = 500;
          const ctx = canvasRef.current.getContext("2d");
          canvasRef.current.width = img.width;
          canvasRef.current.height = img.height;
          ctx?.drawImage(img, 0, 0, img.width, img.height);
          const base64data = canvasRef.current.toDataURL();
          setDataBase64(base64data);
          console.log(base64data);
        }
      };
    };
    setFile(target.files[0]);
    reader.readAsDataURL(target.files[0]);
  }
  const handleTranslate = async () => {
    try {
      setLoading(true);
      if (dataBase64) {
        const parse = dataBase64.slice(dataBase64.indexOf(",") + 1);
        const body = {
          image: parse,
        };
        console.log("body:", body);

        // Here you can change the API endpoint
        const imagePost = await fetch("api/translate", {
          method: "POST",
          mode: "no-cors",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(body),
        });
        const response = await imagePost.json();
        const newData = "data:image/jpg;base64," + response.image;
        console.log("translated image: ", newData);
        // Creating Image
        const newImg = new Image();
        setTranslatedImg(newImg);
        newImg.src = newData;
        newImg.width = 500;
        newImg.height = 500;
        newImg.onload = () => {
          const ctx = translatedCanvasRef.current!.getContext("2d");
          translatedCanvasRef.current!.width = newImg.width;
          translatedCanvasRef.current!.height = newImg.height;
          ctx?.drawImage(newImg, 0, 0, newImg.width, newImg.height);
          setLoading(false);
        };
        // }
      } else {
        setDataError("No Image Selected");
        setLoading(false);
      }
    } catch (error) {
      setLoading(false);

      console.log(error);
    }
  };
  return (
    <>
      <Layout>
        <div className="flex min-h-[calc(100vh-100px)]  w-full flex-col items-center bg-gray-950 text-gray-300">
          <div className="mt-8 text-xl font-bold text-gray-400">
            Welcome, here we can communicate with an AI machine.
          </div>
          <div className="min-h-60 mb-14 mt-16 w-[600px] rounded-xl border-2 border-gray-700 p-4">
            <div className="mb-4 text-lg font-bold">Image Translation AI</div>
            <div className="mb-4">Select your image</div>
            <div className="mb-8">
              <input
                id="image"
                type="file"
                name="image"
                accept="image/*"
                className=""
                onChange={handleOnChange}
              />
            </div>
            <div className="flex w-full justify-between">
              <button
                onClick={handleTranslate}
                className="inline-flex items-center rounded-xl border border-green-800 bg-green-400 px-5 py-2 text-center text-lg font-medium text-green-950 transition-all duration-200 hover:border-green-700  hover:bg-green-500 hover:text-green-950 focus:outline-none focus:ring-1 focus:ring-green-600"
              >
                Translate
              </button>
            </div>
          </div>
          <div className="flex w-full justify-around space-x-5 text-xl">
            <div className="">
              {file ? (
                <div className="flex flex-col items-center justify-center">
                  <div className="mb-4 text-gray-300">Selected Image:</div>
                  <div className="flex h-[520px] w-[520px] items-center justify-center overflow-hidden rounded-xl bg-gray-700 text-center">
                    <canvas ref={canvasRef} />
                  </div>
                </div>
              ) : (
                ""
              )}
            </div>
            <div>
              <div
                className={
                  translatedImg
                    ? "flex flex-col items-center justify-center"
                    : "hidden"
                }
              >
                <div className="mb-4 text-gray-300">Translated Image:</div>
                <div className="flex h-[520px] w-[520px] items-center justify-center overflow-hidden rounded-xl bg-gray-700 text-center">
                  <canvas ref={translatedCanvasRef} className="z-10" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </Layout>
    </>
  );
}

export default App;
