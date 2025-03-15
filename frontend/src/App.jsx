import { useState, useEffect } from 'react'
import CityList from './CityList'
import './App.css'

function App() {
  const [cities, setCities] = useState([])

  useEffect(() => {
    fetchCities()
  }, [])
  
  const fetchCities = async () => {
    const response = await fetch("http://127.0.0.1:5000/cities")
    const data = await response.json()
    setCities(data.cities)
    console.log(data.cities)
  }

  return <CityList cities={cities}/>
}

export default App
