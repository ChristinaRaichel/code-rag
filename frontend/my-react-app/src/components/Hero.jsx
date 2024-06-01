import React from 'react'

const Hero = () => {
  const rag_output = [
    {
      pseudo_code: "python tasks = [] while True: task = input('Enter a task or type 'done' to finish: ') if task == 'done': break tasks.append(task) print(f'Your to-do list for today: {tasks}')",
      python_code: "python tasks = [] while True: task = input('Enter a task or type 'done' to finish: ') if task == 'done': break tasks.append(task) print(f'Your to-do list for today: {tasks}')",
      explanation: "python tasks = [] while True: task = input('Enter a task or type 'done' to finish: ') if task == 'done': break tasks.append(task) print(f'Your to-do list for today: {tasks}')",
    }
  ];

  return (
    <div className="grid grid-cols-5 grid-rows-5 gap-4">
    <div className="row-span-2">
        <div className='absolute top-[15%] w-40 flex flex-col text-black p-4'>
          <h2 className='font-bold text-4xl'> Turn your daily tasks into code! </h2>
          <h1 className='font-italic font-thin text-blue-950 '>This tool hooks you up with explanations, pseudocode, and Python code for whatever you're tackling in your day-to-day life</h1>
          <form className='search'>
            <div className='py-5'>
              <p className='search-text'> Search for your task to generate code </p>
              <input type="text" placeholder='Enter your text here..' />
            </div>
          </form>
        </div>
   </div>
    <div className="pseudocode col-span-2 row-span-3"> 
    {
      
      rag_output.map((data, key) => {
        return (
          <div key={key}>
            {data.pseudo_code}
          </div>
        );
      })

    }
    </div>
 
    <div className="col-span-2 row-span-3 col-start-4">
    {
      
      rag_output.map((data, key) => {
        return (
          <div key={key}>
            {data.python_code}
          </div>
        );
      })

    }
    </div>
    <div className="row-span-3 row-start-3">
    
    </div>
    <div className="col-span-4 row-span-2 col-start-2 row-start-4">
    {
      
      rag_output.map((data, key) => {
        return (
          <div key={key}>
            {data.explanation}
          </div>
        );
      })

    }
    </div>

   </div>
   
 
  )
}

export default Hero