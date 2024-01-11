package paddleboat.webcomicspringbackend.model.system;

import lombok.Data;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.MDC;
import org.springframework.http.HttpStatus;

import java.time.Instant;
import java.util.UUID;

@Slf4j
@Data
public class ServiceContext {

    // We will assign variables to this threadLocal and it will remain unique to whatever API call.
    public static InheritableThreadLocal<ServiceContext> threadLocal = new InheritableThreadLocal<>();
    public static String EXECUTION_ID_KEY = "executionId";
    private HttpStatus httpStatus;
    private String executionId;
    private String sessionIp;

    private Instant startTime;
    private Instant endTime;

    private ServiceContext(String executionId) {
        String txnId = executionId;
        if (executionId == null || executionId.isEmpty()) {
            txnId = UUID.randomUUID().toString();
        }
        setExecutionId(txnId);
        this.httpStatus = HttpStatus.OK;

    }

    private void setExecutionId(String txnId) {
        if (txnId == null) {
            log.warn("Txn id was found null at a point! That's not good!");
            txnId = UUID.randomUUID().toString();
        }

        this.executionId = txnId;

        // Sets execution Id on logs
        MDC.put(EXECUTION_ID_KEY, txnId);
    }
    protected static ServiceContext newContext(String executionId) {
        ServiceContext ctx = new ServiceContext(executionId);
        threadLocal.set(ctx);
        return ctx;
    }

    public synchronized static ServiceContext getContext() {
        return getContext(null);
    }

    public synchronized static ServiceContext getContext(String executionId) {
        ServiceContext ctx = threadLocal.get();

        if (ctx == null) {
            ctx = newContext(executionId);
            log.debug("Creating new context. Requested executionId[{}] Context: [{}]", executionId, ctx);
            return ctx;
        }

        // Resetting MDC map with the execution id from the inherited thread
        ctx.setExecutionId(ctx.getExecutionId());
        return ctx;
    }

    public void endServiceCall() {
        this.setEndTime(Instant.now());
    }
}
