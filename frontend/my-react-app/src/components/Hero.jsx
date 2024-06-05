import React from 'react'
import Search from './Search'


const Hero = () => {

  return (
    <div className='absolute top-[15%] w-40 flex flex-col text-black p-4'>
      <h2 > Turn your daily tasks into code! </h2>
      <h1 className='font-italic font-thin text-blue-950 '>
        This tool hooks you up with explanations, pseudocode, and Python code for whatever you're tackling in your day-to-day life</h1>
      <form className='search'>
        <div className='py-5'>
        <Search />
        </div>
      </form>
    </div>

  
   
 
  )
}

export default Hero