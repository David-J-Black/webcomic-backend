package paddleboat.webcomicspringbackend.model.system;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Configuration;
import org.springframework.lang.NonNull;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@RequiredArgsConstructor
@Slf4j
public class WebConfig implements WebMvcConfigurer {

    private final ServiceContextInterceptor serviceContextInterceptor;

    @Override
    public void addInterceptors(@NonNull InterceptorRegistry registry) {
        log.info("Adding interceptors...");
        try {
            registry.addInterceptor(this.serviceContextInterceptor);
        } catch (RuntimeException e) {
            log.error("Problem establishing Interceptors!", e);
            throw e;
        }

    }

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        long MAX_AGE_SECONDS = 3600;
        registry.addMapping("/**")
                .allowedOrigins("http://localhost:4200")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
                .allowedHeaders("*")
                .allowCredentials(true).maxAge(MAX_AGE_SECONDS);
    }
}
