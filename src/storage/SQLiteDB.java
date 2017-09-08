package storage;

import model.PointOfInterest;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public final class SQLiteDB implements Database {
    private static final SQLiteDB instance = new SQLiteDB();
    private static final String name = "points.db";

    static {
        String sql = "CREATE TABLE IF NOT EXISTS PointsOfInterest (name STRING PRIMARY KEY, x INTEGER, y INTEGER)";
        updateSQL(sql);
    }

    private SQLiteDB() {}

    public static SQLiteDB getInstance() {
        return instance;
    }

    private static void updateSQL(String sql) {
        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:" + name)) {
            Statement statement = connection.createStatement();
            statement.executeUpdate(sql);
        }

        catch (SQLException e) {}
    }

    @Override
    public void addPOI(PointOfInterest poi) {
        String sql = String.format("INSERT INTO PointsOfInterest VALUES (\"%s\", %d, %d);",
                                    poi.getName(), poi.getX(), poi.getY());
        updateSQL(sql);
    }

    @Override
    public List<PointOfInterest> listPOIs() {
        String sql = "SELECT name, x, y FROM PointsOfInterest";
        ArrayList<PointOfInterest> pois = new ArrayList<>();

        try (Connection connection = DriverManager.getConnection("jdbc:sqlite:" + name)) {
            Statement statement = connection.createStatement();
            ResultSet data = statement.executeQuery(sql);

            while (data.next())
                pois.add(new PointOfInterest(data.getString("name"), data.getInt("x"), data.getInt("y")));
        }

        catch (SQLException e) {}

        return pois;
    }

    @Override
    public List<PointOfInterest> listNearbyPOIs(int x, int y, int dMax) {
        ArrayList<PointOfInterest> nearby = new ArrayList<>();
        int dx, dy;

        for (PointOfInterest poi: this.listPOIs()) {
            dx = poi.getX() - x;
            dy = poi.getY() - y;

            if (Math.sqrt(dx * dx + dy * dy) <= dMax)
                nearby.add(poi);
        }

        return nearby;
    }
}
