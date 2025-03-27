import React from 'react'

function Navbar() {
  return (
    <div>
      <div className="navbar bg-base-100 shadow-sm">
  <div className="flex-1">
    <a className="btn btn-ghost text-xl">ScholarPage</a>
  </div>
  <div className="flex-none">
    <button className='btn'>Log In</button>
  </div>
</div>
    </div>
  )
}

export default Navbar
