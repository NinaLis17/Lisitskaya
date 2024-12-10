import java.time.LocalTime;

class Station {
    private String name;
    private LocalTime arrivalTime;
    private LocalTime departureTime;

    public Station(String name, LocalTime arrivalTime, LocalTime departureTime) {
        this.name = name;
        this.arrivalTime = arrivalTime;
        this.departureTime = departureTime;
    }

    public String getName() {
        return name;
    }

    public LocalTime getArrivalTime() {
        return arrivalTime;
    }

    public LocalTime getDepartureTime() {
        return departureTime;
    }
}