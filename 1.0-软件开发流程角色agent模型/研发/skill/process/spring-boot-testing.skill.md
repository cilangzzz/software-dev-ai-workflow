---
name: spring-boot-testing
description: Expert Spring Boot 4 testing specialist that selects the best Spring Boot testing techniques for your situation with Junit 6 and AssertJ.
---

# Spring Boot Testing

This skill provides expert guide for testing Spring Boot 4 applications with modern patterns and best practices.

## Core Principles

1. **Test Pyramid**: Unit (fast) > Slice (focused) > Integration (complete)
2. **Right Tool**: Use the narrowest slice that gives you confidence
3. **AssertJ Style**: Fluent, readable assertions over verbose matchers
4. **Modern APIs**: Prefer MockMvcTester and RestTestClient over legacy alternatives

## Which Test Slice?

| Scenario | Annotation | Reference |
|----------|------------|-----------|
| Controller + HTTP semantics | `@WebMvcTest` | references/webmvctest.md <!-- TODO: references/webmvctest.md 缺失 --> |
| Repository + JPA queries | `@DataJpaTest` | references/datajpatest.md <!-- TODO: references/datajpatest.md 缺失 --> |
| REST client + external APIs | `@RestClientTest` | references/restclienttest.md <!-- TODO: references/restclienttest.md 缺失 --> |
| JSON (de)serialization | `@JsonTest` | references/test-slices-overview.md <!-- TODO: references/test-slices-overview.md 缺失 --> |
| Full application | `@SpringBootTest` | references/test-slices-overview.md <!-- TODO: references/test-slices-overview.md 缺失 --> |

## Test Slices Reference

- references/test-slices-overview.md <!-- TODO: references/test-slices-overview.md 缺失 --> - Decision matrix and comparison
- references/webmvctest.md <!-- TODO: references/webmvctest.md 缺失 --> - Web layer with MockMvc
- references/datajpatest.md <!-- TODO: references/datajpatest.md 缺失 --> - Data layer with Testcontainers
- references/restclienttest.md <!-- TODO: references/restclienttest.md 缺失 --> - REST client testing

## Testing Tools Reference

- references/mockmvc-tester.md <!-- TODO: references/mockmvc-tester.md 缺失 --> - AssertJ-style MockMvc (3.2+)
- references/mockmvc-classic.md <!-- TODO: references/mockmvc-classic.md 缺失 --> - Traditional MockMvc (pre-3.2)
- references/resttestclient.md <!-- TODO: references/resttestclient.md 缺失 --> - Spring Boot 4+ REST client
- references/mockitobean.md <!-- TODO: references/mockitobean.md 缺失 --> - Mocking dependencies

## Assertion Libraries

- references/assertj-basics.md <!-- TODO: references/assertj-basics.md 缺失 --> - Scalars, strings, booleans, dates
- references/assertj-collections.md <!-- TODO: references/assertj-collections.md 缺失 --> - Lists, Sets, Maps, arrays

## Testcontainers

- references/testcontainers-jdbc.md <!-- TODO: references/testcontainers-jdbc.md 缺失 --> - PostgreSQL, MySQL, etc.

## Test Data Generation

- references/instancio.md <!-- TODO: references/instancio.md 缺失 --> - Generate complex test objects (3+ properties)

## Performance & Migration

- references/context-caching.md <!-- TODO: references/context-caching.md 缺失 --> - Speed up test suites
- references/sb4-migration.md <!-- TODO: references/sb4-migration.md 缺失 --> - Spring Boot 4.0 changes

## Quick Decision Tree

```
Testing a controller endpoint?
  Yes → @WebMvcTest with MockMvcTester

Testing repository queries?
  Yes → @DataJpaTest with Testcontainers (real DB)

Testing business logic in service?
  Yes → Plain JUnit + Mockito (no Spring context)

Testing external API client?
  Yes → @RestClientTest with MockRestServiceServer

Testing JSON mapping?
  Yes → @JsonTest

Need full integration test?
  Yes → @SpringBootTest with minimal context config
```

## Spring Boot 4 Highlights

- **RestTestClient**: Modern alternative to TestRestTemplate
- **@MockitoBean**: Replaces @MockBean (deprecated)
- **MockMvcTester**: AssertJ-style assertions for web tests
- **Modular starters**: Technology-specific test starters
- **Context pausing**: Automatic pausing of cached contexts (Spring Framework 7)

## Testing Best Practices

### Code Complexity Assessment

When a method or class is too complex to test effectively:

1. **Analyze complexity** - If you need more than 5-7 test cases to cover a single method, it's likely too complex
2. **Recommend refactoring** - Suggest breaking the code into smaller, focused functions
3. **User decision** - If the user agrees to refactor, help identify extraction points
4. **Proceed if needed** - If the user decides to continue with the complex code, implement tests despite the difficulty

**Example of refactoring recommendation:**
```java
// Before: Complex method hard to test
public Order processOrder(OrderRequest request) {
  // Validation, discount calculation, payment, inventory, notification...
  // 50+ lines of mixed concerns
}

// After: Refactored into testable units
public Order processOrder(OrderRequest request) {
  validateOrder(request);
  var order = createOrder(request);
  applyDiscount(order);
  processPayment(order);
  updateInventory(order);
  sendNotification(order);
  return order;
}
```

### Avoid Code Redundancy

Create helper methods for commonly used objects and mock setup to enhance readability and maintainability.

### Test Organization with @DisplayName

Use descriptive display names to clarify test intent:

```java
@Test
@DisplayName("Should calculate discount for VIP customer")
void shouldCalculateDiscountForVip() { }

@Test
@DisplayName("Should reject order when customer has insufficient credit")
void shouldRejectOrderForInsufficientCredit() { }
```

### Test Coverage Order

Always structure tests in this order:

1. **Main scenario** - The happy path, most common use case
2. **Other paths** - Alternative valid scenarios, edge cases
3. **Exceptions/Errors** - Invalid inputs, error conditions, failure modes

### Test Production Scenarios

Write tests with real production scenarios in mind. This makes tests more relatable and helps understand code behavior in actual production cases.

### Test Coverage Goals

Aim for 80% code coverage as a practical balance between quality and effort. Higher coverage is beneficial but not the only goal.

Use Jacoco maven plugin for coverage reporting and tracking.


**Coverage Rules:**
- 80+% coverage minimum
- Focus on meaningful assertions, not just execution

**What to Prioritize:**
1. Business-critical paths (payment processing, order validation)
2. Complex algorithms (pricing, discount calculations)
3. Error handling (exceptions, edge cases)
4. Integration points (external APIs, databases)

## Dependencies (Spring Boot 4)

```xml
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-test</artifactId>
  <scope>test</scope>
</dependency>

<!-- For WebMvc tests -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-webmvc-test</artifactId>
  <scope>test</scope>
</dependency>

<!-- For Testcontainers -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-testcontainers</artifactId>
  <scope>test</scope>
</dependency>
```
