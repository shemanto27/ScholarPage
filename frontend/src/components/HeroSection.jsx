import React from 'react'
import { FaArrowRight } from "react-icons/fa";

function HeroSection() {
  return (
    <div>
      <div className="hero bg-base-200 min-h-screen">
  <div className="hero-content flex-col lg:flex-row">
    <img
      src="https://img.daisyui.com/images/stock/photo-1635805737707-575885ab0820.webp"
      className="max-w-sm rounded-lg shadow-2xl" />
    <div>
      <h1 className="text-5xl font-bold">Showcase your research profile with beautiful website</h1>
      <p className="py-6">
      Create a beautiful research profile that highlights your publications, citations, and achievements—effortlessly. Join researchers worldwide in showcasing your academic journey!
      </p>
      <div className='flex gap-2'>
        <div>
        <label className="input validator">
        <p>scholarpage.me/</p>
        <input type="input" required placeholder="Username" pattern="[A-Za-z][A-Za-z0-9\-]*" minlength="3" maxlength="30" title="Only letters, numbers or dash" />
        </label>
        <p className="validator-hint ">
        Must be 3 to 30 characters
        <br/>containing only letters, numbers or dash
        </p>
        </div>
        
            <button className="btn btn-primary">CLAIM YOUR SCHOLAR PAGE <FaArrowRight /></button>
      </div>
    </div>
  </div>
</div>
    </div>
  )
}

export default HeroSection
