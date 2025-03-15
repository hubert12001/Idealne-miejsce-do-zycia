
const CityList = ({cities}) => {
    return <div>
        <h2>Miasta</h2>
        <table>
            <thead>
                <tr>
                    <th>Nazwa miasta</th>
                    <th>Populacja</th>
                    <th>Koszt życia</th>
                </tr>
            </thead>
            <tbody>
                {cities.map((city) => (
                    <tr key={city.id}>
                        <td>{city.name}</td>
                        <td>{city.population}</td>
                        <td>{city.costOfLiving}</td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default CityList