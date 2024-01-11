package paddleboat.webcomicspringbackend.service;

import jakarta.annotation.PostConstruct;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import paddleboat.webcomicspringbackend.service.cache.ComicCache;

@Service
@RequiredArgsConstructor
@Slf4j
public class CacheService {

    private final ComicCache comicCache;

    @PostConstruct
    public void init() {
        try {
            log.debug("Loading Cache");
            comicCache.load();
        } catch (Exception e) {
            log.error("Problem loading cache!", e);
            throw e;
        }
    }

}
