import java.util.ArrayList;
import java.util.List;

public class Route {
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

    public void removeStation(Station station) {
        stations.remove(station);
    }

    public void updateStation(int index, Station station) {
        if (index >= 0 && index < stations.size()) {
            stations.set(index, station);
        } else {
            System.out.println("Индекс вне диапазона.");
        }
    }

    public void printRoute() {
        System.out.println("Номер поезда: " + trainNumber + ", Название маршрута: " + routeName);
        for (Station station : stations) {
            System.out.println(station);
        }
    }
}

