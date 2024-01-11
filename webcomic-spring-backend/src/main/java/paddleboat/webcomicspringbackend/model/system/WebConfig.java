package paddleboat.webcomicspringbackend.model.system;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@RequiredArgsConstructor
@Slf4j
public class WebConfig implements WebMvcConfigurer {

    private final ServiceContextInterceptor serviceContextInterceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        log.debug("Adding interceptors...");
        try {
            registry.addInterceptor(this.serviceContextInterceptor);
        } catch (Exception e) {
            log.error("Problem establishing Interceptors!", e);
        }

    }

}
