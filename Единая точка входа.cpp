#include <iostream>
#include <string>
#include <map>
#include <functional> // std::function

// Базовый класс контроллера (абстрактный)
class Controller {
public:
    virtual void handleRequest(const std::string& request) = 0; // Чисто виртуальная функция
    virtual ~Controller() {} // Виртуальный деструктор для полиморфизма
};

// Конкретный контроллер 1
class UserController : public Controller {
public:
    void handleRequest(const std::string& request) override {
        std::cout << "UserController handles request: " << request << std::endl;
        // Здесь может быть логика, связанная с пользователями
    }
};

// Конкретный контроллер 2
class ProductController : public Controller {
public:
    void handleRequest(const std::string& request) override {
        std::cout << "ProductController handles request: " << request << std::endl;
        // Здесь может быть логика, связанная с продуктами
    }
};

// Класс Router (Единая точка входа)
class Router {
public:
    // Добавить маршрут
    void addRoute(const std::string& route, Controller* controller) {
        routes[route] = controller;
    }

    // Обработать запрос
    void handleRequest(const std::string& request) {
        // Найти подходящий контроллер
        auto it = routes.find(request);
        if (it != routes.end()) {
            it->second->handleRequest(request);
        } else {
            std::cout << "Error: No route found for request: " << request << std::endl;
        }
    }

private:
    std::map<std::string, Controller*> routes; // Маршруты и соответствующие контроллеры
};

int main() {
    // Создаем экземпляры контроллеров
    UserController* userController = new UserController();
    ProductController* productController = new ProductController();

    // Создаем экземпляр маршрутизатора
    Router router;

    // Регистрируем маршруты
    router.addRoute("/users", userController);
    router.addRoute("/products", productController);

    // Обрабатываем запросы
    router.handleRequest("/users");
    router.handleRequest("/products");
    router.handleRequest("/unknown"); // Запрос к несуществующему маршруту

    // Освобождаем память (важно делать!)
    delete userController;
    delete productController;

    return 0;
}