import java.util.ArrayList;
import java.util.List;

class Route {
    private String trainNumber;
    private String routeName;
    private List<Station> stations;

    public Route(String trainNumber, String routeName) {
        this.trainNumber = trainNumber;
        this.routeName = routeName;
        this.stations = new ArrayList<>();
    }

    public void addStation(Station station) {
        stations.add(station);
    }

    public List<Station> getStations() {
        return stations;
    }

    public String getTrainNumber() {
        return trainNumber;
    }

    public String getRouteName() {
        return routeName;
    }
}