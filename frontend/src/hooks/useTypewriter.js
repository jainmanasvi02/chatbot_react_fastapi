import { useState, useEffect } from "react";

export default function useTypewriter(text="", speed = 50) {
  const [displayedText, setDisplayedText] = useState("");

  useEffect(() => {
    let index = 0;
    let timeoutId;

    setDisplayedText(""); 

    const typeNext = () => {
        if (index < text.length) {
            const nextChar = text.charAt(index);
            setDisplayedText((prev) => prev + nextChar);
            index++;
            timeoutId = setTimeout(typeNext, speed);
        }
    };

    timeoutId = setTimeout(typeNext, speed); 

    return () => clearTimeout(timeoutId); // To do cleanup on text change
  }, [text, speed]);

  return displayedText;
}
