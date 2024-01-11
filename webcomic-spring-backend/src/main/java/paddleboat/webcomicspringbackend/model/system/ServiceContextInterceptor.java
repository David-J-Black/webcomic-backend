package paddleboat.webcomicspringbackend.model.system;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.lang.NonNull;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.util.WebUtils;

@Slf4j
@Component
public class ServiceContextInterceptor implements HandlerInterceptor {

    public static String EXECUTION_ID_HEADER = "executionId";

    @Override
    public boolean preHandle(@NonNull HttpServletRequest request,
                             @NonNull HttpServletResponse response,
                             @NonNull Object handler) {
        this.startNewServiceContext(request);
        return true;
    }

    private void startNewServiceContext(HttpServletRequest request) {
        String requestIp = WebUtils.getSessionId(request);
        log.info("Started call [{}] for IP [{}]", request.getRequestURI(), requestIp);

        String executionId = request.getHeader(EXECUTION_ID_HEADER);
    }

}
