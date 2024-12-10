import java.sql.*;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        DatabaseConnection.loadDriver();

        try (Connection connection = DatabaseConnection.getConnection()) {
            initializeDatabase(connection);

            Scanner scanner = new Scanner(System.in);
            while (true) {
                System.out.println("1. Создать маршрут");
                System.out.println("2. Вывести маршруты");
                System.out.println("3. Выход");
                System.out.print("Выберите действие: ");
                int choice = scanner.nextInt();
                scanner.nextLine();

                switch (choice) {
                    case 1:
                        createRoute(scanner, connection);
                        break;
                    case 2:
                        printRoutes(connection);
                        break;
                    case 3:
                        System.out.println("Выход из программы.");
                        return;
                    default:
                        System.out.println("Неверный выбор. Попробуйте еще раз.");
                }
            }

        } catch (SQLException e) {
            System.err.println("Error connecting to database: " + e.getMessage());
        }
    }

    private static void initializeDatabase(Connection connection) throws SQLException {
        Statement statement = connection.createStatement();
        statement.execute("CREATE TABLE IF NOT EXISTS routes (id INTEGER AUTO_INCREMENT PRIMARY KEY, trainNumber VARCHAR(255), routeName VARCHAR(255))");
        statement.execute("CREATE TABLE IF NOT EXISTS stations (routeID INTEGER, stationName VARCHAR(255), arrivalTime TIME, departureTime TIME, PRIMARY KEY (routeID, stationName), FOREIGN KEY (routeID) REFERENCES routes(id))");
    }

    private static void createRoute(Scanner scanner, Connection connection) throws SQLException {
        System.out.print("Введите номер поезда: ");
        String trainNumber = scanner.nextLine();
        System.out.print("Введите название маршрута: ");
        String routeName = scanner.nextLine();

        Route route = new Route(trainNumber, routeName);

        while (true) {
            System.out.print("Введите название станции (или 'выход' для завершения): ");
            String stationName = scanner.nextLine();
            if (stationName.equalsIgnoreCase("выход")) break;

            System.out.print("Введите время прибытия (чч:мм): ");
            LocalTime arrivalTime = LocalTime.parse(scanner.nextLine());
            System.out.print("Введите время отправления (чч:мм): ");
            LocalTime departureTime = LocalTime.parse(scanner.nextLine());

            route.addStation(new Station(stationName, arrivalTime, departureTime));
        }

        saveRouteToDB(connection, route);
    }

    private static void printRoutes(Connection connection) throws SQLException {
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery("SELECT * FROM routes");

        while (resultSet.next()) {
            int routeId = resultSet.getInt("id");
            String trainNumber = resultSet.getString("trainNumber");
            String routeName = resultSet.getString("routeName");
            System.out.println("Маршрут ID: " + routeId + ", Номер поезда: " + trainNumber + ", Название маршрута: " + routeName);
            printStations(connection, routeId);
        }
    }

    private static void printStations(Connection connection, int routeId) throws SQLException {
        PreparedStatement preparedStatement = connection.prepareStatement("SELECT * FROM stations WHERE routeID = ?");
        preparedStatement.setInt(1, routeId);
        ResultSet resultSet = preparedStatement.executeQuery();

        while (resultSet.next()) {
            String stationName = resultSet.getString("stationName");
            Time arrivalTime = resultSet.getTime("arrivalTime");
            Time departureTime = resultSet.getTime("departureTime");
            System.out.println("  Станция: " + stationName + ", Время прибытия: " + arrivalTime + ", Время отправления: " + departureTime);
        }
    }

    private static void saveRouteToDB(Connection connection, Route route) throws SQLException {
        PreparedStatement preparedStatement = null;

        try {
            preparedStatement = connection.prepareStatement("INSERT INTO routes (trainNumber, routeName) VALUES (?, ?)", Statement.RETURN_GENERATED_KEYS);
            preparedStatement.setString(1, route.getTrainNumber());
            preparedStatement.setString(2, route.getRouteName());
            preparedStatement.executeUpdate();

            ResultSet generatedKeys = preparedStatement.getGeneratedKeys();
            int routeId = -1;

            if (generatedKeys.next()) {
                routeId = generatedKeys.getInt(1);
            }

            preparedStatement = connection.prepareStatement("INSERT INTO stations (routeID, stationName, arrivalTime, departureTime) VALUES (?, ?, ?, ?)");
            for (Station station : route.getStations()) {
                preparedStatement.setInt(1, routeId);
                preparedStatement.setString(2, station.getName());
                preparedStatement.setTime(3, Time.valueOf(station.getArrivalTime()));
                preparedStatement.setTime(4, Time.valueOf(station.getDepartureTime()));
                preparedStatement.executeUpdate();
            }
        } finally {
            if (preparedStatement != null) preparedStatement.close();
        }
    }
}