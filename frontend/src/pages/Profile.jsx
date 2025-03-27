import React from 'react'
import { IoPersonSharp } from "react-icons/io5";
import { IoColorPaletteSharp } from "react-icons/io5";
import { IoStatsChart } from "react-icons/io5";
import { IoSettingsSharp } from "react-icons/io5";
import { IoSparkles } from "react-icons/io5";
import { FaLocationDot } from "react-icons/fa6";
import { FaUniversity } from "react-icons/fa";
import { MdEmail } from "react-icons/md";
import { TbCategoryFilled } from "react-icons/tb";
import { TiPlus } from "react-icons/ti";
import { MdDeleteForever } from "react-icons/md";

function Profile() {
  return (
    <>
    {/* Deploy Button */}
    <div className="bg-base-100 shadow-sm">
        <div className="flex justify-end">
        <a className="btn m-2">Deploy<IoSparkles /></a>
        </div>
    </div>

    {/* Navbar */}
    <div className=" bg-base-100 shadow-sm">
        <div className=" flex justify-around gap-4 p-2">
        <a className="btn"><IoPersonSharp />Page</a>
        <a className="btn"><IoColorPaletteSharp />Style</a>
        <a className="btn"><IoStatsChart />Stats</a>
        <a className="btn"><IoSettingsSharp />Settings</a>
        </div>
    </div>


    {/* Basic Info Card */}
    <div className="card bg-base-100 shadow-sm w-full">
  <div className="card-body">
        {/* Full Name and Profile pic */}
        <div className='flex flex-row gap-1 w-full'>
            {/* Profile pic */}
            <div className="avatar">
            <div className="w-10 rounded-full">
                <img src="https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.webp" />
            </div>
            </div>

            {/* Full Name */}
            <label className="input validator">
            <input type="input" required placeholder="Full Name" pattern="[A-Za-z][A-Za-z0-9\-]*" minlength="3" maxlength="30" title="Only letters, numbers or dash" />
            </label>
            <p className="validator-hint">
            Must be 3 to 30 characters
            <br/>containing only letters, numbers or dash
            </p>
        </div>

        {/* Bio */}
        <fieldset className="fieldset">
            <textarea className="textarea h-24" placeholder="Bio"></textarea>
        </fieldset>

        {/* Extra Info Buttons */}
        <div className='flex justify-between gap-2'>
            <button className='btn'><FaLocationDot /></button>
            <button className='btn'><FaUniversity /></button>
            <button className='btn'><MdEmail /></button>
            <button className='btn'><TbCategoryFilled /></button>
        </div>
    </div>
    </div>

    {/* Add Publication */}
    <hr className='my-3 border-2 border-b-neutral-400'/>
    <div className="card bg-base-100 shadow-sm w-full">
    <div className="card-body">
        {/* Publication Title */}
            <label className="input ">
            <input type="input" required placeholder="Publication/Project Title"/>
            </label>

        {/* Say something about your work */}
        <label className="input ">
            <input type="input" maxlength='250' required placeholder="write something about your work in 250 words"/>
        </label>

        {/* Category */}
        <label className="input ">
            <input type="input" required placeholder="Category"/>
        </label>

        {/* Year of Publication */}
        <label className="input ">
            <input type="input" required placeholder="Year of Publication"/>
        </label>

    <div className='flex gap-2'>       
        <button className='btn btn-success flex-grow'><TiPlus /> Add Publications/Projects</button>
        <button className='btn btn-error'><MdDeleteForever className='text-2xl'/></button>
    </div>
    </div>
    </div>
    </>
  )
}

export default Profile
