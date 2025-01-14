const RestaurantHours = ({ hours }) => {
  const daysOfWeek = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];

  return (
    <table className="hours-table">
      <tbody>
        {daysOfWeek.map((day) => {
          const times = hours[day];
          return (
            <tr key={day}>
              <td className="day-cell">
                <strong>{day}</strong>
              </td>
              <td>
                {times && times.open !== "Closed" && times.close !== "Closed"
                  ? `${times.open} - ${times.close}`
                  : "Closed"}
              </td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

export default RestaurantHours;
