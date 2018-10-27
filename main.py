Entity employee = new Entity("Employee", "asalieri");
employee.setProperty("firstName", "Antonio");
employee.setProperty("lastName", "Salieri");
employee.setProperty("hireDate", new Date());
employee.setProperty("attendedHrTraining", true);

DatastoreService datastore = DatastoreServiceFactory.getDatastoreService();
datastore.put(employee);
