import java.time.LocalTime;

public class Main {
    public static void main(String[] args) {
        Route route = new Route("123", "Москва - Санкт-Петербург");
        Route route2 = new Route("6408", "Воронеж - Лиски");

        route.addStation(new Station("Москва", LocalTime.of(10, 0), LocalTime.of(10, 30)));
        route.addStation(new Station("Тверь", LocalTime.of(12, 0), LocalTime.of(12, 15)));
        route.addStation(new Station("Санкт-Петербург", LocalTime.of(14, 0), LocalTime.of(14, 0)));
        route2.addStation(new Station("Воронеж 1", LocalTime.of(8, 30), LocalTime.of(8, 34)));

        route.printRoute();
        route2.printRoute();

        route.updateStation(1, new Station("Тверь", LocalTime.of(12, 5), LocalTime.of(12, 20)));

        route.removeStation(new Station("Москва", LocalTime.of(10, 0), LocalTime.of(10, 30)));

        System.out.println("\nОбновленный маршрут:");
        route.printRoute();
    }
}
